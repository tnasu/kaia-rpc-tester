rm -rf cn/data/klay/chaindata/ cn/data/klay/LOCK cn/data/klay/transactions.rlp cn/data/keystore/UTC--* *.profile *.trace
cn/bin/kcn init --datadir cn/data genesis.json
cn/bin/kcnd start
