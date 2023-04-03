import pandas
import argparse
import ip
import sys

def main():
    args = input_args()

    ip_dict = {}

    parse_csv(args.file, ip_dict)

    print("YUZHOU DEBUG", ip_dict["206.189.50.226"].whois.text)

    data = []
    for ip_obj in ip_dict.values():
        data.append(ip_obj.output())
    
    output_df = pandas.DataFrame(data, columns=ip.IP.output_header())
    output_df.to_csv("output.csv")


def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="CSV file path")

    return parser.parse_args()

def parse_csv(file, ip_dict):
    df = pandas.read_csv(file)
    df = df.reset_index()

    for index, row in df.iterrows():
        print_progress(int(index/len(df.index)*100))

        request_ip = row["request_ip"]

        if request_ip not in ip_dict:
            ip_dict[request_ip] = ip.IP(request_ip, row["user_agent"], row["count"])
        else:
            ip_dict[request_ip].update(row["count"])

    print()

def print_progress(i):
    sys.stdout.write('\r')
    sys.stdout.write("[%-100s] %d%%" % ('='*i, i))
    sys.stdout.flush()

if __name__ == "__main__":
    main()
