def extract_groups(filename):
    end = []
    # print(T[1])
    with open(filename, "r") as file:
        for line in file:
            numbers_str = line.strip().split()
            if numbers_str:
                numbers = [float(s) for s in numbers_str]
                # print(len(numbers))
            if len(end) < 1:
                end = [numbers_str]
            else:
                end.extend([numbers_str])
        return end
