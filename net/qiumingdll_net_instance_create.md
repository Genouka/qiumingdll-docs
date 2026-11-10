# qiumingdll_net_instance_create()

创建一个“共享实例”（同步对象），并同步给房间内所有端。

## 函数签名

```gml
qiumingdll_net_instance_create(type, state_json)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 是 | 实例类型名，自定义，例如 `"enemy"`、`"bullet"`；用于接收端区分对象种类 |
| state_json | string | 是 | 初始状态的 **JSON 字面量**，例如 `"{\"x\":10,\"y\":20}"` |

## 返回值

| 值 | 说明 |
|----|------|
| host：`> 0` | 新实例 id（从 1 开始递增，断开/销毁后**不复用**） |
| client：`1` | 请求已发出（**异步**）：真实 id 需要从 `poll_json()` 的 `op="create"` 事件中获取 |
| `0` | 失败：未连接，或发送失败 |

## 使用说明

- 实例是 host 仲裁的：client 的创建请求会先发给 host，由 host 统一分配 id 并广播给**所有**端（包括发起者）。
- 因此 client 侧不要用返回值当 id；请按以下方式接入：
  1. 调用 `instance_create` 记下“我发起了一次创建”；
  2. 下一帧从 `poll_json()` 里取 `kind="instance"`、`op="create"` 且 type/state 匹配的事件，用其中的 `id` 作为真实对象 id。
- host 调用时，除了广播，也会给自己入队同样的 create 事件（`peer=0`），消费方式与 client 完全一致。
- 新 client 加入时，WELCOME 快照会为所有已存在实例各入队一条 `op="create"` 事件，所以“上线即同步”无需额外代码。
- 实例本身不会自动销毁；离开房间、切换场景时请自行 `instance_destroy` 或由 host 统一清理。

## 示例

```gml
// Step 事件：处理实例创建事件
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "instance" && _e.op == "create")
    {
        var _obj = instance_create_depth(_e.state.x, _e.state.y, 0, obj_remote_actor);
        _obj.netId = _e.id;
        _obj.netType = _e.type;
    }
}

// 本地创建（host 或 client 都可调用）
qiumingdll_net_instance_create("enemy", "{\"x\":100,\"y\":64}");
```

## 相关函数

- [qiumingdll_net_instance_update](qiumingdll_net_instance_update.md)
- [qiumingdll_net_instance_destroy](qiumingdll_net_instance_destroy.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_fire_event](qiumingdll_net_fire_event.md)
