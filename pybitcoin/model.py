from typing import List
from enum import IntEnum
from pydantic import BaseModel, SecretStr
from pybitcoin.types import *
from .address import Address
from .addressdescriptor import AddressDescriptor
from .extpubkey import ExtPubKey
from .multisigsecret import MultisigSecret
from .outpoint import Outpoint
from .pubkey import PubKey
from .recipient import Recipient
from .utxodescriptor import UtxoDescriptor
from .walletsecret import WalletSecret


class Model(BaseModel):
    """A Model template."""
    class Config:
        json_encoders = {
            Address: lambda v: str(v),
            bool: lambda v: str(v).lower(),
            bytes: lambda v: v.hex(),
            IntEnum: lambda v: v.value,
            SecretStr: lambda v: v.get_secret_value(),
            Money: lambda v: str(v),
            hexstr: lambda v: str(v),
            ExtPubKey: lambda v: str(v),
            PubKey: lambda v: str(v),
            int32: lambda v: str(v),
            uint32: lambda v: str(v),
            int64: lambda v: str(v),
            uint64: lambda v: str(v),
            uint128: lambda v: str(v),
            uint160: lambda v: str(v),
            uint256: lambda v: str(v),
            List[str]: lambda v: ','.join(v),
            List[Address]: lambda v: ','.join([str(x) for x in v]),
            List[AddressDescriptor]: lambda v: [x.json() for x in v],
            List[MultisigSecret]: lambda v: [x.json() for x in v],
            List[Recipient]: lambda v: [x.json() for x in v],
            List[Outpoint]: lambda v: [x.json() for x in v],
            List[UtxoDescriptor]: lambda v: [x.json() for x in v],
            List[WalletSecret]: lambda v: [x.json() for x in v]
        }
        allow_population_by_field_name = True
    
    def json(self, *args, **kwargs) -> str:
        return super(Model, self).json(exclude_none=True, by_alias=True)
