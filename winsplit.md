# winsplit 模块

窗口分裂功能（GPU D3D11 钩子方案）。将游戏窗口内容渲染到多个独立的子窗口中。

## 技术原理

- 通过 vtable patch 钩住 `IDXGISwapChain::Present`
- 在 Present 调用前同步读取 backbuffer（类似 glReadPixels）
- 使用 DWM Cloak（Win8+）隐藏原窗口
- 零延迟，与游戏帧同步

## 基础 API

### qmWinSplitInit

```c
QM_EXPORT QM_Real qmWinSplitInit(QM_String hwndParam);
```

**参数：**
- `hwndParam` - 源窗口句柄（字符串形式）

**返回值：**
- `0` - 成功
- 非零 - 失败

---

### qmWinSplitCreate

```c
QM_EXPORT QM_Real qmWinSplitCreate(
    QM_Real srcX, QM_Real srcY, QM_Real srcW, QM_Real srcH,
    QM_Real dstX, QM_Real dstY, QM_Real dstW, QM_Real dstH
);
```

**参数：**
- `srcX, srcY, srcW, srcH` - 源区域（原窗口中的截取区域）
- `dstX, dstY, dstW, dstH` - 目标位置和大小（分裂窗口）

**返回值：**
- 分裂窗口 ID（1-16），0 表示失败

---

### qmWinSplitDestroy

```c
QM_EXPORT QM_Real qmWinSplitDestroy(QM_Real splitId);
```

**参数：**
- `splitId` - 分裂窗口 ID

---

### qmWinSplitDestroyAll

```c
QM_EXPORT QM_Real qmWinSplitDestroyAll();
```

**说明：** 销毁所有分裂窗口

---

### qmWinSplitSetPosition

```c
QM_EXPORT QM_Real qmWinSplitSetPosition(QM_Real splitId, QM_Real x, QM_Real y);
```

---

### qmWinSplitSetSize

```c
QM_EXPORT QM_Real qmWinSplitSetSize(QM_Real splitId, QM_Real w, QM_Real h);
```

---

### qmWinSplitSetRegion

```c
QM_EXPORT QM_Real qmWinSplitSetRegion(QM_Real splitId, QM_Real x, QM_Real y, QM_Real w, QM_Real h);
```

**说明：** 同时设置位置和大小

---

### qmWinSplitShow / qmWinSplitHide

```c
QM_EXPORT QM_Real qmWinSplitShow(QM_Real splitId);
QM_EXPORT QM_Real qmWinSplitHide(QM_Real splitId);
```

---

### qmWinSplitHideOriginal / qmWinSplitShowOriginal

```c
QM_EXPORT QM_Real qmWinSplitHideOriginal();
QM_EXPORT QM_Real qmWinSplitShowOriginal();
```

**说明：** 使用 DWM Cloak 隐藏/显示原窗口

---

### qmWinSplitSetSourceRegion

```c
QM_EXPORT QM_Real qmWinSplitSetSourceRegion(
    QM_Real splitId, QM_Real srcX, QM_Real srcY, QM_Real srcW, QM_Real srcH
);
```

**说明：** 设置分裂窗口截取的源区域

---

### qmWinSplitGetInfo

```c
QM_EXPORT QM_Real qmWinSplitGetInfo(QM_Real splitId, QM_Real infoType);
```

**infoType：**
- `0` - X 坐标
- `1` - Y 坐标
- `2` - 宽度
- `3` - 高度
- `4` - 是否可见

---

### qmWinSplitGetCount

```c
QM_EXPORT QM_Real qmWinSplitGetCount();
```

**返回值：** 活跃的分裂窗口数量

---

### qmWinSplitExists

```c
QM_EXPORT QM_Real qmWinSplitExists(QM_Real splitId);
```

**返回值：**
- `1.0` - 存在
- `0.0` - 不存在

---

### qmWinSplitCleanup

```c
QM_EXPORT QM_Real qmWinSplitCleanup();
```

**说明：** 清理所有分裂窗口和钩子

## 形状 API

### qmWinSplitBeginShape / qmWinSplitEndShape

```c
QM_EXPORT QM_Real qmWinSplitBeginShape(QM_Real splitId);
QM_EXPORT QM_Real qmWinSplitEndShape(QM_Real splitId);
```

**说明：** 开始/结束形状定义（用于多边形裁剪）

---

### qmWinSplitAddShapePoint

```c
QM_EXPORT QM_Real qmWinSplitAddShapePoint(QM_Real splitId, QM_Real x, QM_Real y);
```

---

### qmWinSplitSetShapeEllipse

```c
QM_EXPORT QM_Real qmWinSplitSetShapeEllipse(QM_Real splitId);
```

---

### qmWinSplitSetShapeRoundRect

```c
QM_EXPORT QM_Real qmWinSplitSetShapeRoundRect(QM_Real splitId, QM_Real cornerW, QM_Real cornerH);
```

---

### qmWinSplitSetShapeFromBitmap

```c
QM_EXPORT QM_Real qmWinSplitSetShapeFromBitmap(QM_Real splitId, QM_String bitmapPath, QM_Real transColor);
```

**说明：** 从位图文件创建形状（transColor 为透明色 RGB 值）

---

### qmWinSplitClearShape

```c
QM_EXPORT QM_Real qmWinSplitClearShape(QM_Real splitId);
```

## 窗口外观 API

| 函数 | 参数 | 说明 |
|------|------|------|
| `qmWinSplitSetDraggable` | splitId, draggable(0/1) | 设置是否可拖拽 |
| `qmWinSplitSetTopmost` | splitId, topmost(0/1) | 设置是否置顶 |
| `qmWinSplitSetOpacity` | splitId, opacity(0-255) | 设置透明度 |
| `qmWinSplitSetTitleBar` | splitId, hasTitleBar(0/1) | 设置标题栏 |
| `qmWinSplitSetTitle` | splitId, title | 设置标题文本 |
| `qmWinSplitSetClosable` | splitId, closable(0/1) | 设置是否可关闭 |
| `qmWinSplitSetCloseTriggersMain` | splitId, triggers(0/1) | 关闭时是否关闭主窗口 |

## 动画 API

### 缓动曲线类型

| 值 | 类型 | 说明 |
|----|------|------|
| 0 | Linear | 线性 |
| 1 | EaseIn | 加速 |
| 2 | EaseOut | 减速 |
| 3 | EaseInOut | 加速后减速 |
| 4 | EaseInCubic | 三次加速 |
| 5 | EaseOutCubic | 三次减速 |
| 6 | EaseInOutCubic | 三次加速后减速 |
| 7 | EaseInBack | 回退加速 |
| 8 | EaseOutBack | 回退减速 |
| 9 | EaseInOutBack | 回退加速后减速 |
| 10 | EaseBounceOut | 弹跳效果 |
| 11 | EaseElasticOut | 弹性效果 |

### 基本动画

```c
// 设置缓动曲线
qmWinSplitSetEasingCurve(splitId, curve);

// 设置源区域动画模式
qmWinSplitSetSrcAnimMode(splitId, mode);

// 位置动画
qmWinSplitSetPositionAnimate(splitId, x, y, totalMs, intervalMs);

// 尺寸动画
qmWinSplitSetSizeAnimate(splitId, w, h, totalMs, intervalMs);

// 区域动画
qmWinSplitSetRegionAnimate(splitId, x, y, w, h, totalMs, intervalMs);

// 停止动画
qmWinSplitStopAnimation(splitId);

// 检查是否正在动画
qmWinSplitIsAnimating(splitId);
```

### 路径动画

```c
// 添加路径点
qmWinSplitAddPathPoint(splitId, x, y);

// 清空路径
qmWinSplitClearPath(splitId);

// 执行路径动画
qmWinSplitMovePath(splitId);
qmWinSplitMovePathAnimate(splitId, totalMs, intervalMs);
```

### 批处理动画

```c
// 开始批处理
qmWinSplitBatchBegin(splitId);

// 设置批处理参数
qmWinSplitBatchSetEasing(splitId, easing);
qmWinSplitBatchSetSrcAnimMode(splitId, mode);

// 添加动画步骤
qmWinSplitBatchAddPosition(splitId, x, y, durationMs);
qmWinSplitBatchAddSize(splitId, w, h, durationMs);
qmWinSplitBatchAddRegion(splitId, x, y, w, h, durationMs);
qmWinSplitBatchAddSrcRegion(splitId, srcX, srcY, srcW, srcH, durationMs);
qmWinSplitBatchAddWait(splitId, durationMs);

// 结束并播放
qmWinSplitBatchEnd(splitId);
qmWinSplitBatchPlay(splitId, conflictMode);
qmWinSplitBatchPlayFrameSync(splitId, conflictMode);

// 控制
qmWinSplitBatchStep(splitId);
qmWinSplitBatchStop(splitId);
qmWinSplitBatchIsPlaying(splitId);
qmWinSplitBatchClear(splitId);
```

### 冲突模式

| 值 | 模式 | 说明 |
|----|------|------|
| 0 | Stack | 堆叠 |
| 1 | Interrupt | 中断 |
| 2 | Rollback | 回滚 |
| 3 | FastForward | 快进 |

## 弃用 API

以下 API 保留为 no-op，新方案不再使用：

- `qmWinSplitSetCaptureMode` - 旧方案切换截图模式
- `qmWinSplitSetCaptureClientOnly` - 旧方案只截客户区
- `qmWinSplitSetDwmThumbnailMode` - 旧方案使用 DWM 缩略图
- `qmWinSplitSetRenderInterval` - 旧方案限制渲染帧率
- `qmWinSplitSetStretchMode` - GDI 拉伸模式（仍可用于 BitBlt）
- `qmWinSplitSetRenderDuringDrag` - 拖拽时是否渲染（仍保留功能）
