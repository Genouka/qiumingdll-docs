# qiumingdll_net_instance_destroy()

销毁一个共享实例，并同步给房间内所有端。

## 函数签名

```gml
qiumingdll_net_instance_destroy(id)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | real | 是 | 要销毁的实例 id |

## 返回值

| 值 | 说明 |
|----|------|
| host：`1` | 实例存在，已删除并广播 |
| host：`0` | 实例不存在（重复销毁或从未创建），未广播 |
| client：`1` | 请求已发给 host（异步） |
| client：`0` | 发送失败或未连接 |

## 使用说明

- host 从实例表删除后广播，并给自己入队 `op="destroy"` 事件（`peer=0`）。
- 销毁事件的 `state` 字段固定为 `null`，`type` 为该实例的原类型，因此接收端无需再查表即可区分类型。
- 实例 id 销毁后不会被重新分配。
- 重复销毁是安全的：host 第二次返回 `0`，不会产生重复事件。
- 玩家离开房间时，其创建但未销毁的实例**不会自动清理**；如需“人走怪清”，请在 host 侧收到该 peer 的 disconnect 事件后统一销毁（可在实例上记录 owner，或由业务方维护映射）。

## 示例

```gml
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "instance" && _e.op == "destroy")
    {
        var _inst = net_find_instance(_e.id);
        if (_inst != noone) instance_destroy(_inst);
    }
}

// 本地销毁（host 或 client 都可调用）
if (qiumingdll_net_instance_destroy(_inst.netId))
{
    instance_destroy(_inst);  // 本地也立即清掉；重复销毁事件到达时按 id 找不到即可忽略
}
```

## 相关函数

- [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md)
- [qiumingdll_net_instance_update](qiumingdll_net_instance_update.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
