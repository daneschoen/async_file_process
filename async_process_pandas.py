from concurrent.futures import ThreadPoolExecutor

def process_file(fname: str, std_len: list = [5, 10, 15]):  # note: ordinary def
    sym = dict()
    df = pd.read_csv(fname)
    df.sort_values(by=['blockTime'], inplace=True)
    for s in df['collectionSymbol'].unique():
        sym[s] = df[df['collectionSymbol'] == s]
        for std_time in std_len:
            sym[s]['std_' + str(std_time)] = df['price'].rolling(std_time).std()

    return sym

def concurrent_threads(fnames: list):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, fname)
                   for fname in fnames]
        concurrent.futures.wait(futures)



