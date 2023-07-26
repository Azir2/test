from model import Vehicle, Log

def main():
    # 使用例子：
    vehicle = Vehicle()
    log = Log()

    # 启动
    vehicle.start(log)

    # 添加目标
    vehicle.add_destination(10, 10, log)

    # 更新目标
    vehicle.update_destination(0, 20, 20, log)

    # 移动
    while vehicle.status == "moving":
        vehicle.move(log)

    # 停止
    vehicle.stop(log)

if __name__ == '__main__':
    main()