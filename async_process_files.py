import asyncio
import aiofiles


async def async_file_process(fname: str, hdr_lst: list) -> dict:
    symbols = dict()
    async with aiofiles.open(fname) as f:
        async for line in f:
            rec = [_.strip() for _ in line.split(',')]
            rec_sym = rec[hdr_lst.index('collectionSymbol')]
            rec_typ = rec[hdr_lst.index('type')]
            rec_prc = rec[hdr_lst.index('price')]
            rec_dtime = rec[hdr_lst.index('blockTime')]
            if rec_sym == '' or rec_typ == '' or rec_prc == '':
                pass
            if rec_sym not in symbols:
                    symbols[rec_sym] = {'bid':0.0, 'list':0.0}
            if rec_typ == 'bid':
                if symbols[rec_sym]['bid'] < symbols[rec_sym].get('bid',0.0):
                    symbols[rec_sym]['bid'] = rec_prc
            elif rec_typ == 'list':
                if symbols[rec_sym]['list'] > symbols[rec_sym].get('list',0.0):
                    symbols[rec_sym]['list'] = rec_prc
            elif rec_typ == 'list':
                if symbols[rec_sym]['list'] > symbols[rec_sym].get('list',0.0):
                    symbols[rec_sym]['list'] = rec_prc

    return symbols


async def async_files(fname_lst: list, hdr_lst: list) -> list:

    tasks = []
    sym_files = []
    for fname in fname_lst:
        tasks.append(
            asyncio.ensure_future(
                sym.files.apppend(async_file_process(fname, hdr_lst))
            )
        )
    await asyncio.gather(*tasks)

    return sym_files


if __name__ == '__main__':
    fname_lst = ['verylargefile.csv']
    hdr = "blockTime,buyer,collection,collectionSymbol,price,seller,signature,slot,source,tokenMint,type"
    hdr_lst = [col for col in hdr.split(',')]

    asyncio.run(async_files(fname_lst, hdr_lst))

