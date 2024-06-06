import subprocess


def nmap_scan(target, ports='1-65535', options='-F -T4'):
    """
    使用nmap进行端口扫描

    参数:
        target (str): 要扫描的目标IP或域名
        ports (str): 要扫描的端口范围，默认为'1-65535'
        options (str): nmap的选项，默认为'-F -T4'（快速模式，时间模板4）

    返回:
        str: nmap扫描的输出结果
    """
    command = ['nmap', options, '-p', ports, target]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print(f"Error occurred: {result.stderr}")
        return None

    return result.stdout


# 示例使用
target = '192.168.1.1'  # 替换为你要扫描的目标IP或域名
output = nmap_scan(target)
if output:
    print(output)