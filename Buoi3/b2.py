def TinhDoKho(old_target, time_start, time_end): 
    actual_time = time_end - time_start 
    expected_time = 2016 * 10 * 60  
    ratio = actual_time / expected_time 
    if ratio < 0.25:
        ratio = 0.25
    if ratio > 4.00:
        ratio = 4.00 
    new_target = int(old_target * ratio)
    return actual_time, ratio, new_target

old_target_hex = "000000000000000000084bc771b929b0780276b1c31cec10a96921b1e53b970a"
old_target = int(old_target_hex, 16)

# Đào trong 7 ngày
t_start = 1600000000 
t_end = 1600000000 + (7 * 24 * 60 * 60) 
# Đào trong 50 ngày
t_start1 = 1600000000 
t_end1 = 1600000000 + (50 * 24 * 60 * 60)

actual_s, adj_ratio, target_n = TinhDoKho(old_target, t_start, t_end)
print("Đào trong 7 ngày:")
print(f" - Thời gian thực tế: {actual_s / 60} phút")
print(f" - Tỷ lệ điều chỉnh: {adj_ratio:.4f}")
print(f" - Target mới (Hex): {target_n:064x}")

print("\nĐào trong 50 ngày:")
actual_s1, adj_ratio1, target_n1 = TinhDoKho(old_target, t_start1, t_end1)
print(f" - Thời gian thực tế: {actual_s1 / 60} phút")
print(f" - Tỷ lệ điều chỉnh: {adj_ratio1:.4f}")
print(f" - Target mới (Hex): {target_n1:064x}")

