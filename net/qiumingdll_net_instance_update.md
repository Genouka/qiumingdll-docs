# qiumingdll_net_instance_update()

更新一个共享实例的状态（整体替换），并同步给房间内所有端。

## 函数签名

```gml
qiumingdll_net_instance_update(id, state_json)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | real | 是 | 目标实例 id（host 分配的 id，或 poll 事件中的 `id`） |
| state_json | string | 是 | 新的状态 **JSON 字面量**，例如 `"{\"x\":120,\"y\":64}"` |

## 返回值

| 值 | 说明 |
|----|------|
| host：`1` | 实例存在，已更新并广播 |
| host：`0` | 实例不存在（可能已被销毁），未做任何广播 |
| client：`1` | 请求已发给 host（异步）；host 接受后会广播 update 事件 |
| client：`0` | 发送失败或未连接 |

## 使用说明

- 状态是**整体替换**，不是字段合并：本次 `state_json` 就是该实例的新状态，未包含的字段即视为不存在。需要合并请在本地先组装好完整状态。
- 采用“最后写入胜出”策略，不做冲突检测与帧同步；高频更新（如每帧坐标）建议降低发送频率（例如每 2~4 帧一次）或自行插值。
- host 更新后会给自己入队 `op="update"` 事件（`peer=0`），所有 client 也会收到同一条广播。
- 对不存在的 id 更新：host 返回 `0`；client 仍返回 `1`（因为发送成功），以实际是否收到 update 事件为准。
- 收到的 `state` 在 destroy 事件中为 `null`，其余事件为 JSON 对象。

## 示例

```gml
// host：权威更新某个实例的位置
qiumingdll_net_instance_update(_inst.netId, "{\"x\":" + string(_inst.x) + ",\"y\":" + string(_inst.y) + "}");

// client：上报自己的输入/位置（host 决定是否采纳）
qiumingdll_net_instance_update(myNetId, "{\"inputX\":1,\"inputY\":0}");

// 接收端
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "instance" && _e.op == "update")
    {
        var _inst = net_find_instance(_e.id);
        if (_inst != noone) net_apply_state(_inst, _e.state);
    }
}
```

## 相关函数

- [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md)
- [qiumingdll_net_instance_destroy](qiumingdll_net_instance_destroy.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
