import psutil  # type: ignore


def get_system_metrics():

    """
        This API gets System Metrics(Cpu, Memory, Disk, System Helath)
        Based on cpu Threshold i.e 25 (configurable)
    """

    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent


    cpu_thersold = 25

    status = "HIGH CPU" if cpu_percent > cpu_thersold  else "Healthy"

    return {
        "cpu_percentage" : cpu_percent,
        "memory_percentage" : memory_percent,
        "disk_percentage" : disk_percent,
        "cpu_threshold" : cpu_thersold,
        "system_status" : status
    }