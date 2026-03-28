def calculate_times(sequence):
    time_test = 0
    time_scan = 0

    result = []

    for job in sequence:
        start_test = time_test
        finish_test = start_test + job['test']
        time_test = finish_test

        start_scan = max(finish_test, time_scan)
        finish_scan = start_scan + job['scan']
        time_scan = finish_scan

        result.append({
            'patient': job['name'],
            'test_start': start_test,
            'test_end': finish_test,
            'scan_start': start_scan,
            'scan_end': finish_scan
        })

    makespan = time_scan

    idle_time_scan = 0
    prev_end = 0
    for r in result:
        if r['scan_start'] > prev_end:
            idle_time_scan += r['scan_start'] - prev_end
        prev_end = r['scan_end']

    return result, makespan, idle_time_scan