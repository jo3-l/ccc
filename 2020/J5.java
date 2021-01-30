import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;

public class J5 {
	public static final int END_ROOM_TOKEN = -1;

	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int maxRows = Integer.parseInt(reader.readLine());
		int maxColumns = Integer.parseInt(reader.readLine());

		int[][] matrix = new int[maxRows][maxColumns];
		StringBuilder buffer = new StringBuilder();
		for (int i = 0; i < maxRows; i++) {
			int[] row = matrix[i];
			outer: for (int j = 0; j < maxColumns; j++) {
				while (true) {
					int c = reader.read();
					if (c == -1) {
						row[j] = Integer.parseInt(buffer.toString());
						break outer;
					}
					;
					if (c == ' ' || c == '\n') {
						row[j] = Integer.parseInt(buffer.toString());
						buffer.setLength(0);
						continue outer;
					}
					;
					buffer.append((char) c);
				}
			}
		}
		matrix[maxRows - 1][maxColumns - 1] = END_ROOM_TOKEN;

		reader.close();

		BreadthFirstSearch bfs = new BreadthFirstSearch(matrix[0][0], matrix, maxRows, maxColumns);
		System.out.println(bfs.canExit() ? "yes" : "no");
	}

	private static class BreadthFirstSearch {
		private final int[][] matrix;
		private final int maxRows;
		private final int maxColumns;
		private final Deque<Integer> queuedValues = new ArrayDeque<>();
		private final Set<Integer> visitedValues = new HashSet<>();

		private BreadthFirstSearch(int initialValue, int[][] matrix, int maxRows, int maxColumns) {
			this.matrix = matrix;
			this.maxRows = maxRows;
			this.maxColumns = maxColumns;

			queuedValues.add(initialValue);
		}

		public boolean canExit() {
			while (!queuedValues.isEmpty()) {
				int topValue = queuedValues.pop();

				int lowerBound = (int) Math.ceil((float) topValue / Math.max(maxRows, maxColumns));
				int upperBound = maxRows + 1;
				for (int possibleRow = lowerBound; possibleRow < upperBound; possibleRow++) {
					if (topValue % possibleRow == 0) {
						int matchingColumn = topValue / possibleRow;
						if (matchingColumn > maxColumns)
							continue;
						if (this.queueMove(possibleRow - 1, matchingColumn - 1))
							return true;

						if (possibleRow != matchingColumn) {
							if (matchingColumn > maxRows || possibleRow > maxColumns)
								continue;
							if (this.queueMove(matchingColumn - 1, possibleRow - 1))
								return true;
						}
					}
				}
			}

			return false;
		}

		private boolean queueMove(int row, int column) {
			int value = matrix[row][column];
			if (value == END_ROOM_TOKEN)
				return true;
			if (visitedValues.contains(value))
				return false;

			this.visitedValues.add(value);
			this.queuedValues.add(value);
			return false;
		}
	}
}
