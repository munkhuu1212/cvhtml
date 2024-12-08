import java.util.*;

public class Lab_8_3 {
    public static int[] assignBikes(int[][] students, int[][] bikes) {
        // Оюутан, дугуй хоорондын зайг хадгалсан жагсаалтыг үүсгэнэ
        List<int[]> distances = new ArrayList<>();

        // Оюутан бүрийн хувьд бүх дугуйнуудын зайг тооцоолно
        for (int i = 0; i < students.length; i++) {
            for (int j = 0; j < bikes.length; j++) {
                int dist = Math.abs(students[i][0] - bikes[j][0]) + Math.abs(students[i][1] - bikes[j][1]);
                distances.add(new int[]{dist, i, j});
            }
        }

        // Зай, дараа нь оюутан, дараа нь дугуйг тоогоор нь эрэмбэлнэ
        distances.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });

        // Оюутан болон дугуйг сонгож байгаа эсэхийг тэмдэглэнэ
        int[] assigned = new int[students.length];
        Arrays.fill(assigned, -1);
        boolean[] usedBikes = new boolean[bikes.length];

        // Эрэмбэлсэн зайг ашиглан хамгийн ойр байгааг оюутанд даатгана
        for (int[] d : distances) {
            @SuppressWarnings("unused")
            int dist = d[0], student = d[1], bike = d[2];
            if (assigned[student] == -1 && !usedBikes[bike]) {
                assigned[student] = bike;
                usedBikes[bike] = true;
            }
        }

        return assigned;
    }

    public static void main(String[] args) {
        int[][] students = {{0, 0}, {1, 1}};
        int[][] bikes = {{0, 1}, {4, 3}, {2, 1}};
        System.out.println(Arrays.toString(assignBikes(students, bikes)));  // Гаралт: [0, 2]
    }
}