
# src/key_management.py
from bip_utils import Bip39SeedGenerator, Bip44Coins, Bip44, base58, Bip44Changes

def get_solana_address_pk(mnemonic, password=''):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate(password)
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)
    bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)
    priv_key_bytes = bip44_chg_ctx.PrivateKey().Raw().ToBytes()
    public_key_bytes = bip44_chg_ctx.PublicKey().RawCompressed().ToBytes()[1:]
    key_pair = priv_key_bytes + public_key_bytes

    return bip44_chg_ctx.PublicKey().ToAddress(), base58.Base58Encoder.Encode(key_pair)
