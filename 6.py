from collections import OrderedDict

def get_transactions(a):
    stats = OrderedDict()
    for tx in a:
        if tx == "print_it":
            for k, v in stats.items():
                print(f"{k}: сумма {v['value']}, количество {v['count']}")
        else:
            op_type, value = tx.split('-')[1].split(':')
            value = int(value)
            if op_type not in stats:
                stats[op_type] = {"value": 0, "count": 0}
            stats[op_type]["value"] += value
            stats[op_type]["count"] += 1
