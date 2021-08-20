import re
from collections import Counter


class LogFileExtractor:

    def __init__(self):
        file1 = open('C:/Ramya/log_file_sample.txt')
        self.lines = file1.readlines()
        print(len(self.lines))

    def log_extract(self):
        info_list, error_list, warn_list = self.log_type_extract(self.lines)
        print(len(info_list))
        print(len(error_list))
        print(len(warn_list))
        self.log_extract_time_based(info_list, error_list, warn_list)

    @staticmethod
    def log_type_extract(lines):
        info_list = []
        error_list = []
        warn_list = []
        for line in lines:
            if 'INFO' in line:
                info_list.append(line)
            elif 'ERROR' in line:
                error_list.append(line)
            elif 'WARN' in line:
                warn_list.append(line)
        return info_list, error_list, warn_list

    @staticmethod
    def log_extract_time_based(info_list, error_list, warn_list):
        imatch_list = []
        ematch_list = []
        wmatch_list = []
        regex = r'(.*)\s([0-9]{2}:[0-9]{2}:[0-9]{2})\s(INFO|ERROR|WARN)\s(.*)'
        for line in info_list:
            for match in re.finditer(regex, line, re.S):
                match_groups = match.groups()
                imatch_list.append(match_groups[1].split(':')[0])
        info_count = Counter(sorted(imatch_list))
        print(info_count)
        for line in error_list:
            for match in re.finditer(regex, line, re.S):
                match_groups = match.groups()
                ematch_list.append(match_groups[1].split(':')[0])
        error_count = Counter(sorted(ematch_list))
        print(error_count)

        for line in warn_list:
            for match in re.finditer(regex, line, re.S):
                match_groups = match.groups()
                wmatch_list.append(match_groups[1].split(':')[0])
        warn_count = Counter(sorted(wmatch_list))
        print(warn_count)


pipeline = LogFileExtractor()
pipeline.log_extract()
