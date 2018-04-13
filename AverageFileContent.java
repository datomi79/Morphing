package morphing.avg;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class AverageFileContentNew {

	public static void main(String[] args) throws IOException {
		
		String path = "F:\\Capstone Project\\2_New Video For Journal Only Proposed\\2_AddExtraPoints\\ThresholdDyn\\";
		File folder = new File(path);
		File[] listOfFiles = folder.listFiles();

		// sort the array
		Arrays.sort(listOfFiles, new Comparator<File>() {
			@Override
			public int compare(File f1, File f2) {
				try {
					return f1.getName().compareTo(f2.getName()) ;
				} catch (NumberFormatException e) {
					throw new AssertionError(e);
				}
			}
		});

		long start = System.currentTimeMillis();

		String LastName = "**", CurrentName;
		for (int j = 0; j < listOfFiles.length; j++) {
			CurrentName = listOfFiles[j].getName();

			if (j > 0) {
				String input1 = path + LastName;
				String input2 = path + CurrentName;

				BufferedReader br1 = new BufferedReader(new FileReader(input1));

				BufferedReader br2 = new BufferedReader(new FileReader(input2));

				String line1;
				String line2;

				String line1_element1, line1_element2;
				String line2_element1, line2_element2;

				String filename1 = LastName.substring(0, LastName.lastIndexOf("."));
				String filename2 = CurrentName.substring(0, CurrentName.lastIndexOf("."));

				String p = "F:\\Capstone Project\\2_New Video For Journal Only Proposed\\3_FileAvg\\ThresholdDyn\\";
				String FILENAME = p + "avg_" + filename1 + "_" + filename2 + ".txt";
				FileWriter fw = new FileWriter(FILENAME);
				BufferedWriter bw = new BufferedWriter(fw);

				while (true) {
					line1 = br1.readLine();
					line2 = br2.readLine();

					if (line1 == null || line2 == null)
						break;

					line1_element1 = line1.split(" ")[0];
					line1_element2 = line1.split(" ")[1];

					line2_element1 = line2.split(" ")[0];
					line2_element2 = line2.split(" ")[1];

					int average1 = (Integer.valueOf(line1_element1) + Integer.valueOf(line2_element1)) / 2;
					int average2 = (Integer.valueOf(line1_element2) + Integer.valueOf(line2_element2)) / 2;

					String content = average1 + " " + average2;

					bw.write(content + "\n");
				}

				// System.out.println(FILENAME + "Created");
				br1.close();
				br2.close();
				bw.close();
			}

			LastName = CurrentName;
		}

		System.out.println("Total Time Taken: " + (System.currentTimeMillis() - start));

	}

}
