
import sys

sys.path.append("../pywallet/")
from pywallet import wallet

if __name__ == '__main__':

    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()

    # create bitcoin wallet
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)

    print(w)

