organize_RP4 is algorithm that uses a csv file containing the data obtained from the A-site estimation algorithm (RPF-build), and aligns it to the .csv output of other programs that look for polybasic domains (for instance: adenosine_sequence, arg_lys_sequence, arg_lys_stretches), in the format of a list of pairs [Gene name, position of the domain].

Usage (on terminal):
organize_RP4.py <RP_data> <polybasic_domains_list> <window_length> <output_file>

RP_data: RP file containing the count of reads from the A-site estimation algorithm
polybasic_domains_list: List obtained as output from the polybasic domains algorithm
window_length: number of codons before and after the polybasic domain that will be shown on output
output_file: Name of the output file for this algorithm