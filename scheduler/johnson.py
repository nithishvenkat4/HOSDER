def johnsons_rule(jobs):
    left = []
    right = []

    for job in jobs:
        if job['test'] <= job['scan']:
            left.append(job)
        else:
            right.append(job)

    left = sorted(left, key=lambda x: x['test'])
    right = sorted(right, key=lambda x: x['scan'], reverse=True)

    return left + right