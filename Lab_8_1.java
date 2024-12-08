import java.util.Arrays;

public class Lab_8_1 {
    public static int coinChange(int[] coins, int amount) {
        // DP массивыг асар том тоогоор инициалжуулна
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;  // Эхний нөхцөл: 0 зоосоор 0 утгыг гаргах боломжтой

        // Бүх зооснуудыг шалгана
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                // Хэрэв өмнөх зоосоор хийсэн тоо боломжтой бол хамгийн бага утгыг олно
                if (dp[i - coin] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        // Хэрэв dp[amount] асар том тоотой байвал боломжгүй гэсэн үг, үгүй бол хамгийн бага тоог буцаана
        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        int amount = 11;
        System.out.println(coinChange(coins, amount));  // Гаралт: 3
    }
}
// 1. Coin Change Problem (Зоосны солилцооны асуудал):
// (Time Complexity): O(n * amount), энд n нь зоосны тоо.
// (Space Complexity): O(amount), учир нь DP массивыг ашиглаж байгаа.