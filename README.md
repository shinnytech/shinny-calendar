# shinny-calendar

获取期货交易日的工具，不依赖任何第三方库

默认包含 2003-2025 年的中国节假日信息。
默认交易日切换时间为 20:00。

## 使用示例

```python
from shinny_calendar import CalendarUtility
calendar = CalendarUtility()
print(calendar.today())
print(calendar.now())
print(calendar.trading_day())
```
