def batch_5wide(epoch):
    k = (epoch // 5) % 4
    return int(2 ** k)