def min_cost_to_jump(n, k, heights):
    # Khởi tạo mảng dp với giá trị vô cùng lớn
    dp = [float('inf')] * n
    dp[0] = 0  # Chi phí tại hòn đá đầu tiên là 0

    # Duyệt qua các hòn đá từ 2 đến n
    for i in range(1, n):
        # Kiểm tra các hòn đá trong phạm vi nhảy từ i-k đến i-1
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(heights[i] - heights[i - j]))

    # Trả về chi phí tối thiểu để đến hòn đá cuối cùng
    return dp[n - 1]

# Nhập dữ liệu đầu vào
n, k = map(int, input("Nhập số lượng hòn đá và giới hạn nhảy: ").split())
heights = list(map(int, input("Nhập độ cao các hòn đá: ").split()))

# Tính toán và in kết quả
result = min_cost_to_jump(n, k, heights)
print("Chi phí tối thiểu để nhảy đến hòn đá cuối cùng là:", result)
