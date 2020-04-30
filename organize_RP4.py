import sys
import csv

def main():
	if len(sys.argv) < 5:
		print('usage: organize_RP4.py <RP_data> <polybasic_domains_list> <window_length> <output_file>')
	input_file = sys.argv[1]
	input_file = open(input_file, 'r')
	RP_list = list(csv.reader(input_file, delimiter=';'))

	list_file = sys.argv[2]
	list_file = open(list_file, 'r')
	position_list = list(csv.reader(list_file, delimiter=';'))

#	if sys.argv[4] == 'fullread':
#		frame = 1
#	elif sys.argv[4] == 'A_site':
	frame = 3
#	else:
#		print(sys.argv[4] + ': not valid')
#		sys.exit()

	output_file = open(sys.argv[4], 'w', newline='')
	out_file = csv.writer(output_file, delimiter=';')

	output_list = []

	for RP in RP_list:
		if len(RP) <= 1:
			continue
		for pos in position_list:
			if len(pos) <= 1:
				continue
			if RP[0] == pos[0]:
				RP_values = RP[1:]
				position_value = pos[1]
				build_output(RP[0], RP_values, int(position_value), int(sys.argv[3]), frame, out_file)

def build_output(gene_id, RP_values, position_value, window_length, frame, fout):
	if position_value/frame - window_length - 1 < 0:
		start_pos = 0
	else:
		start_pos = int(position_value/frame) - window_length - 1

	if position_value/frame + window_length > len(RP_values):
		stop_pos = len(RP_values)
	else:
		stop_pos = int(position_value/frame) + window_length

	fout.writerow([gene_id] + RP_values[start_pos:stop_pos])

main()