file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        total = 0
        count = 0

        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                start_index = line.find(':') + 1
                confidence = float(line[start_index:].strip())

                total += confidence
                count += 1

        if count > 0:
            average = total / count
            print("Average spam confidence:", average)
        else:
            print("No lines starting with 'X-DSPAM-Confidence:' found in the file.")

except FileNotFoundError:
    print("File not found:", file_name)
except Exception as e:
    print("An error occurred:", str(e))