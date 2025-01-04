# coding: utf-8
import datetime
from typing import List


def _accounting_day(
    dt: datetime.datetime, change_trading_day_hour: int, change_trading_day_minute: int
) -> datetime.date:
    """
    会计入账日是指从上一个交易日的20点到当天的20点，每个自然日都可以是会计入账日
    
    Args:
        dt (datetime.datetime): 输入的日期时间
        change_trading_day_hour (int): 交易日切换的小时
        change_trading_day_minute (int): 交易日切换的分钟
    
    Returns:
        datetime.date: 会计入账日
    
    Examples:
        >>> _accounting_day(datetime.datetime(2025, 1, 4, 21, 0), 20, 0)
        datetime.date(2025, 1, 5)
        >>> _accounting_day(datetime.datetime(2025, 1, 4, 19, 0), 20, 0)
        datetime.date(2025, 1, 4)
        >>> _accounting_day(datetime.datetime(2025, 1, 4, 20, 0), 20, 0)
        datetime.date(2025, 1, 5)
    """
    dt_time = dt.replace(hour=change_trading_day_hour, minute=change_trading_day_minute, second=0, microsecond=0)
    if dt >= dt_time:
        dt = dt_time + datetime.timedelta(days=1)
    else:
        dt = dt_time
    return dt.date()

def _trading_day(
    dt: datetime.datetime, 
    holidays: List[datetime.date], 
    change_trading_day_hour: int,
    change_trading_day_minute: int
) -> datetime.date:
    """
    期货交易日
    交易日是指从上一个交易日的20点到当天的20点，如果是周六或周日或者节假日，则顺沿到下一个交易日
    
    Args:
        dt (datetime.datetime): 输入的日期时间
        holidays (List[datetime.date]): 节假日列表
        change_trading_day_hour (int): 交易日切换的小时
        change_trading_day_minute (int): 交易日切换的分钟
    
    Returns:
        datetime.date: 交易日
    
    Examples:
        >>> # 测试节假日跳过
        >>> example_holidays = [
        ...     datetime.date(2025, 1, 30), datetime.date(2025, 1, 31), datetime.date(2025, 2, 3), datetime.date(2025, 2, 4)
        ... ]
        >>> _trading_day(datetime.datetime(2025, 1, 30), example_holidays, 20, 0)
        datetime.date(2025, 2, 5)
        
        >>> # 测试周末跳过
        >>> _trading_day(datetime.datetime(2025, 1, 25), example_holidays, 20, 0)
        datetime.date(2025, 1, 27)
        
        >>> # 测试交易日切换时间
        >>> _trading_day(datetime.datetime(2025, 1, 4, 21, 0), example_holidays, 20, 0)
        datetime.date(2025, 1, 6)
    """
    # 使用指定的小时和分钟设置交易日切换时间点
    dt_time = dt.replace(hour=change_trading_day_hour, minute=change_trading_day_minute, second=0, microsecond=0)
    
    # 如果当前时间在交易日切换时间之后，则使用下一天
    if dt >= dt_time:
        dt = dt_time + datetime.timedelta(days=1)
    else:
        dt = dt_time

    # 处理节假日和周末
    standardized_dt = dt.date()
    
    # 使用提供的节假日列表
    holidays = set(holidays)
    
    # 如果提供了节假日列表，则跳过节假日和周末
    while standardized_dt in holidays or standardized_dt.weekday() in {5, 6}:
        standardized_dt += datetime.timedelta(days=1)
    
    return standardized_dt

def _trading_day_end_time(
    dt: datetime.date, change_trading_day_hour: int, change_trading_day_minute: int
) -> datetime.datetime:
    """
    输入一个日期，代表某个交易日，返回它的结束时间。
    
    Args:
        dt (datetime.date): 输入的日期
        change_trading_day_hour (int): 交易日切换的小时
        change_trading_day_minute (int): 交易日切换的分钟
    
    Returns:
        datetime.datetime: 交易日结束时间
    
    Examples:
        >>> _trading_day_end_time(datetime.date(2025, 1, 4), 20, 0)
        datetime.datetime(2025, 1, 4, 19, 59, 59, 999999)
        >>> _trading_day_end_time(datetime.date(2025, 1, 4), 15, 30)
        datetime.datetime(2025, 1, 4, 15, 29, 59, 999999)
    """
    return datetime.datetime.combine(dt, datetime.time(change_trading_day_hour, change_trading_day_minute)) + datetime.timedelta(microseconds=-1)
