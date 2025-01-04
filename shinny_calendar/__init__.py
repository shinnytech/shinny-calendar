"""
Shinny Calendar - 判断交易日的 python 包.

提供交易日、会计日期等日历相关实用工具。
"""

__version__ = "0.1.0"

import datetime
from typing import List, Optional

from shinny_calendar.core import (
    _trading_day, 
    _accounting_day, 
    _trading_day_end_time
)


__all__ = ['CalendarUtility']


# 默认交易日切换时间
DEFAULT_CHANGE_TRADING_DAY_HOUR = 20
DEFAULT_CHANGE_TRADING_DAY_MINUTE = 0

# 默认节假日列表
_DEFAULT_HOLIDAYS = [
    datetime.date.fromisoformat(dt)
    for dt in ["2003-01-01", "2003-01-30", "2003-01-31", "2003-02-03", "2003-02-04", "2003-02-05", "2003-02-06", "2003-02-07", "2003-05-01", "2003-05-02", "2003-05-05", "2003-05-06", "2003-05-07", "2003-10-01", "2003-10-02", "2003-10-03", "2003-10-06", "2003-10-07", "2004-01-01", "2004-01-19", "2004-01-20", "2004-01-21", "2004-01-22", "2004-01-23", "2004-01-26", "2004-01-27", "2004-01-28", "2004-05-03", "2004-05-04", "2004-05-05", "2004-05-06", "2004-05-07", "2004-10-01", "2004-10-04", "2004-10-05", "2004-10-06", "2004-10-07", "2005-01-03", "2005-02-07", "2005-02-08", "2005-02-09", "2005-02-10", "2005-02-11", "2005-02-14", "2005-02-15", "2005-05-02", "2005-05-03", "2005-05-04", "2005-05-05", "2005-05-06", "2005-10-03", "2005-10-04", "2005-10-05", "2005-10-06", "2005-10-07", "2006-01-02", "2006-01-03", "2006-01-30", "2006-01-31", "2006-02-01", "2006-02-02", "2006-02-03", "2006-05-01", "2006-05-02", "2006-05-03", "2006-05-04", "2006-05-05", "2006-10-02", "2006-10-03", "2006-10-04", "2006-10-05", "2006-10-06", "2007-01-01", "2007-01-02", "2007-01-03", "2007-02-19", "2007-02-20", "2007-02-21", "2007-02-22", "2007-02-23", "2007-05-01", "2007-05-02", "2007-05-03", "2007-05-04", "2007-05-07", "2007-10-01", "2007-10-02", "2007-10-03", "2007-10-04", "2007-10-05", "2007-12-31", "2008-01-01", "2008-02-06", "2008-02-07", "2008-02-08", "2008-02-11", "2008-02-12", "2008-04-04", "2008-05-01", "2008-05-02", "2008-06-09", "2008-09-15", "2008-09-29", "2008-09-30", "2008-10-01", "2008-10-02", "2008-10-03", "2009-01-01", "2009-01-02", "2009-01-26", "2009-01-27", "2009-01-28", "2009-01-29", "2009-01-30", "2009-04-06", "2009-05-01", "2009-05-28", "2009-05-29", "2009-10-01", "2009-10-02", "2009-10-05", "2009-10-06", "2009-10-07", "2009-10-08", "2010-01-01", "2010-02-15", "2010-02-16", "2010-02-17", "2010-02-18", "2010-02-19", "2010-04-05", "2010-05-03", "2010-06-14", "2010-06-15", "2010-06-16", "2010-09-22", "2010-09-23", "2010-09-24", "2010-10-01", "2010-10-04", "2010-10-05", "2010-10-06", "2010-10-07", "2011-01-03", "2011-02-02", "2011-02-03", "2011-02-04", "2011-02-07", "2011-02-08", "2011-04-04", "2011-04-05", "2011-05-02", "2011-06-06", "2011-09-12", "2011-10-03", "2011-10-04", "2011-10-05", "2011-10-06", "2011-10-07", "2012-01-02", "2012-01-03", "2012-01-23", "2012-01-24", "2012-01-25", "2012-01-26", "2012-01-27", "2012-04-02", "2012-04-03", "2012-04-04", "2012-04-30", "2012-05-01", "2012-06-22", "2012-10-01", "2012-10-02", "2012-10-03", "2012-10-04", "2012-10-05", "2013-01-01", "2013-01-02", "2013-01-03", "2013-02-11", "2013-02-12", "2013-02-13", "2013-02-14", "2013-02-15", "2013-04-04", "2013-04-05", "2013-04-29", "2013-04-30", "2013-05-01", "2013-06-10", "2013-06-11", "2013-06-12", "2013-09-19", "2013-09-20", "2013-10-01", "2013-10-02", "2013-10-03", "2013-10-04", "2013-10-07", "2014-01-01", "2014-01-31", "2014-02-03", "2014-02-04", "2014-02-05", "2014-02-06", "2014-04-07", "2014-05-01", "2014-05-02", "2014-06-02", "2014-09-08", "2014-10-01", "2014-10-02", "2014-10-03", "2014-10-06", "2014-10-07", "2015-01-01", "2015-01-02", "2015-02-18", "2015-02-19", "2015-02-20", "2015-02-23", "2015-02-24", "2015-04-06", "2015-05-01", "2015-06-22", "2015-09-03", "2015-09-04", "2015-10-01", "2015-10-02", "2015-10-05", "2015-10-06", "2015-10-07", "2016-01-01", "2016-02-08", "2016-02-09", "2016-02-10", "2016-02-11", "2016-02-12", "2016-04-04", "2016-05-02", "2016-06-09", "2016-06-10", "2016-09-15", "2016-09-16", "2016-10-03", "2016-10-04", "2016-10-05", "2016-10-06", "2016-10-07", "2017-01-02", "2017-01-27", "2017-01-30", "2017-01-31", "2017-02-01", "2017-02-02", "2017-04-03", "2017-04-04", "2017-05-01", "2017-05-29", "2017-05-30", "2017-10-02", "2017-10-03", "2017-10-04", "2017-10-05", "2017-10-06", "2018-01-01", "2018-02-15", "2018-02-16", "2018-02-19", "2018-02-20", "2018-02-21", "2018-04-05", "2018-04-06", "2018-04-30", "2018-05-01", "2018-06-18", "2018-09-24", "2018-10-01", "2018-10-02", "2018-10-03", "2018-10-04", "2018-10-05", "2018-12-31", "2019-01-01", "2019-02-04", "2019-02-05", "2019-02-06", "2019-02-07", "2019-02-08", "2019-04-05", "2019-05-01", "2019-05-02", "2019-05-03", "2019-06-07", "2019-09-13", "2019-10-01", "2019-10-02", "2019-10-03", "2019-10-04", "2019-10-07", "2020-01-01", "2020-01-24", "2020-01-27", "2020-01-28", "2020-01-29", "2020-01-30", "2020-01-31", "2020-04-06", "2020-05-01", "2020-05-04", "2020-05-05", "2020-06-25", "2020-06-26", "2020-10-01", "2020-10-02", "2020-10-05", "2020-10-06", "2020-10-07", "2020-10-08", "2021-01-01", "2021-02-11", "2021-02-12", "2021-02-15", "2021-02-16", "2021-02-17", "2021-04-05", "2021-05-03", "2021-05-04", "2021-05-05", "2021-06-14", "2021-09-20", "2021-09-21", "2021-10-01", "2021-10-04", "2021-10-05", "2021-10-06", "2021-10-07", "2022-01-03", "2022-01-31", "2022-02-01", "2022-02-02", "2022-02-03", "2022-02-04", "2022-04-04", "2022-04-05", "2022-05-02", "2022-05-03", "2022-05-04", "2022-06-03", "2022-09-12", "2022-10-03", "2022-10-04", "2022-10-05", "2022-10-06", "2022-10-07", "2023-01-02", "2023-01-23", "2023-01-24", "2023-01-25", "2023-01-26", "2023-01-27", "2023-04-05", "2023-05-01", "2023-05-02", "2023-05-03", "2023-06-22", "2023-06-23", "2023-09-29", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06", "2024-01-01", "2024-02-09", "2024-02-12", "2024-02-13", "2024-02-14", "2024-02-15", "2024-02-16", "2024-04-04", "2024-04-05", "2024-05-01", "2024-05-02", "2024-05-03", "2024-06-10", "2024-09-16", "2024-09-17", "2024-10-01", "2024-10-02", "2024-10-03", "2024-10-04", "2024-10-07", "2025-01-01", "2025-01-28", "2025-01-29", "2025-01-30", "2025-01-31", "2025-02-03", "2025-02-04", "2025-04-04", "2025-05-01", "2025-05-02", "2025-05-05", "2025-06-02", "2025-10-01", "2025-10-02", "2025-10-03", "2025-10-06", "2025-10-07", "2025-10-08"]
]



class CalendarUtility:
    """
    提供交易日历相关的实用工具。

    主要功能:
    - 获取交易日
    - 获取会计日期
    - 获取当前日期和时间
    """
    def __init__(
        self, 
        holidays: Optional[List[datetime.date]] = _DEFAULT_HOLIDAYS, 
        change_trading_day_hour: int = DEFAULT_CHANGE_TRADING_DAY_HOUR, 
        change_trading_day_minute: int = DEFAULT_CHANGE_TRADING_DAY_MINUTE
    ):
        """
        初始化 CalendarUtility 实例。

        Args:
            holidays: 自定义节假日列表，默认为 _DEFAULT_HOLIDAYS
            change_trading_day_hour: 交易日切换小时，默认为 20
            change_trading_day_minute: 交易日切换分钟，默认为 0 
        """
        self.holidays = holidays
        self.change_trading_day_hour = change_trading_day_hour
        self.change_trading_day_minute = change_trading_day_minute

    def trading_day(self, dt: Optional[datetime.datetime] = None) -> datetime.date:
        """
        获取指定日期的交易日。

        Args:
            dt: 输入的日期时间，默认为当前时间

        Returns:
            交易日的日期
        
        Examples:
            >>> calendar_utility = CalendarUtility()
            >>> calendar_utility.trading_day(datetime.datetime(2025, 1, 1))
            datetime.date(2025, 1, 2)
            >>> calendar_utility.trading_day(datetime.datetime(2025, 1, 2))
            datetime.date(2025, 1, 2)
        """
        return _trading_day(dt or self.now(), self.holidays, self.change_trading_day_hour, self.change_trading_day_minute)

    def today(self) -> datetime.date:
        """
        获取当前日期。

        Returns:
            今天的日期
        """
        return datetime.date.today()

    def now(self) -> datetime.datetime:
        """
        获取当前日期时间。

        Returns:
            当前的日期时间
        """
        return datetime.datetime.now()

    def accounting_day(self, dt: Optional[datetime.datetime] = None) -> datetime.date:
        """
        获取指定日期的会计日。

        Args:
            dt: 输入的日期时间，默认为当前时间

        Returns:
            会计日的日期
        
        Examples:
            >>> calendar_utility = CalendarUtility()
            >>> calendar_utility.accounting_day(datetime.datetime(2025, 1, 1))
            datetime.date(2025, 1, 1)
            >>> calendar_utility.accounting_day(datetime.datetime(2025, 1, 2))
            datetime.date(2025, 1, 2)
        """
        return _accounting_day(dt or self.now(), self.change_trading_day_hour, self.change_trading_day_minute)
    
    def trading_day_end_time(self, dt: Optional[datetime.date] = None) -> datetime.datetime:
        """
        获取指定交易日的结束时间。

        Args:
            dt: 输入交易日

        Returns:
            交易日结束时间

        Examples:
            >>> calendar_utility = CalendarUtility()
            >>> calendar_utility.trading_day_end_time(datetime.date(2025, 1, 4))
            datetime.datetime(2025, 1, 4, 19, 59, 59, 999999)
        """
        return _trading_day_end_time(dt or self.today(), self.change_trading_day_hour, self.change_trading_day_minute)