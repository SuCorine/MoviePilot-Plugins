# 呀哈哈封面工坊 · MoviePilot V3 适配版

本目录是 [呀哈哈封面工坊](https://github.com/justzerock/MoviePilot-Plugins) 面向 **MoviePilot V3** 的实现副本，功能与原作者 V2 版（2.2.11）保持一致，仅做 V3 合同迁移。

## 与原 V2 版的差异

| 项目 | V2 原版 | 本 V3 版 |
| --- | --- | --- |
| 导入路径 | `app.core.*` / `app.helper.*` / `app.utils.*` / `app.log` | `app.sdk.config` / `app.sdk.events` / `app.sdk.media` / `app.sdk.services` / `app.sdk.network` / `app.sdk.utilities` / `app.sdk.logging` |
| 基类 | `app.plugins._PluginBase` | `app.sdk.plugin._PluginBase` |
| 版本 | 2.2.11 | **3.0.0** |
| 依赖声明 | `requirements.txt` | `pyproject.toml`（静态 `project.dependencies`） |
| 索引 | `package.v2.json` | 新增 `package.v3.json`，原 V2 条目标记 `"v3": false` |

## 保留的旧路径（V3 暂无 SDK 出口，实测仍可导入）

- `from app.chain.mediaserver import MediaServerChain`
- `from app.schemas import TransferInfo`
- `from app.schemas import ServiceInfo`
- `from app.schemas.types import EventType`

## 未做改动的部分

插件不访问宿主数据库、未使用已删除的 `MusicChain`、`get_api()` 路由不被宿主包装，因此 V3 迁移指南中"数据库与事务""链职责""REST 响应合同"三节无需改动。

## 许可

沿用上游仓库许可证（见仓库根目录 LICENSE）。适配改动仅为导入路径与元数据。
