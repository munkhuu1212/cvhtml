import java.util.Arrays;

public class Lab_8_2 {
    public static int countPrimes(int n) {
        // Хэрэв n нь 2-оос бага байвал 0-ыг буцаана
        if (n < 2) {
            return 0;
        }

        // Бүх тоонуудыг prime гэж үзэж эхэлнэ
        boolean[] primes = new boolean[n + 1];
        Arrays.fill(primes, true);
        primes[0] = primes[1] = false;  // 0 болон 1 нь prime биш

        // n-ын квадрат язгуур хүртэлх бүх тоонуудыг шалгана
        for (int i = 2; i * i <= n; i++) {
            if (primes[i]) {
                // Хэрэв prime байвал түүний бүх үржвэрүүдийг prime биш гэж тэмдэглэнэ
                for (int j = i * i; j <= n; j += i) {
                    primes[j] = false;
                }
            }
        }

        // Prime үнэн утгуудын тоог нийлбэрлэн буцаана
        int count = 0;
        for (boolean prime : primes) {
            if (prime) count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int n = 18;
        System.out.println(countPrimes(n));  // Гаралт: 7
    }
}