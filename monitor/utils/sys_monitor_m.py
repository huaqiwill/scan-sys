"""

"""

import psutil


def memory_usage():
    # 获取内存信息
    memory_info = psutil.virtual_memory()
    print(f"总内存: {memory_info.total / (1024 ** 3):.2f} GB")
    print(f"已用内存: {memory_info.used / (1024 ** 3):.2f} GB")
    print(f"空闲内存: {memory_info.available / (1024 ** 3):.2f} GB")
    print(f"内存使用率: {memory_info.percent}%")
    dict_ = {
        "total": memory_info.total / (1024**3),  # 总内存
        "used": memory_info.used / (1024**3),  # 已用内存
        "available": memory_info.available / (1024**3),  # 空闲内存
        "percent": memory_info.percent,  # 内存使用率
    }
    return dict_


def disk_usage():
    disk_usage = psutil.disk_usage("/")
    print(f"磁盘总容量: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"已用磁盘: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"剩余磁盘: {disk_usage.free / (1024 ** 3):.2f} GB")
    print(f"磁盘使用率: {disk_usage.percent}%")
    dict_ = {
        "total": disk_usage.total / (1024**3),  # 总容量
        "used": disk_usage.used / (1024**3),  # 已用容量
        "free": disk_usage.free / (1024**3),  # 剩余容量
        "percent": disk_usage.percent,  # 磁盘使用率
    }
    return dict_


def network():
    net_io = psutil.net_io_counters()
    print(f"发送的字节数: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
    print(f"接收的字节数: {net_io.bytes_recv / (1024 ** 2):.2f} MB")
    dict_ = {
        "bytes_sent": net_io.bytes_sent / (1024 ** 2),  # 发送的字节数
        "bytes_recv": net_io.bytes_recv / (1024 ** 2),  # 接收的字节数
    }
    return dict_

def cpu():
    # 获取每个 CPU 核心的使用率
    cpu_percent_per_core = psutil.cpu_percent(percpu=True)
    print(f"每个 CPU 核心的使用率: {cpu_percent_per_core}")

    # 获取所有 CPU 核心的平均使用率
    cpu_percent = psutil.cpu_percent()
    print(f"所有 CPU 核心的平均使用率: {cpu_percent}%")