case "$1" in
	stop)
		cn/bin/kcnd stop
    exit 0
		;;
	restart)
		cn/bin/kcnd stop
		rm -rf cn/data/kcn/logs/kcnd.out
		rm -rf cn/data/kcn/logs/vm.out
		rm -rf ../reports/*
		rm -rf ../testReport/*
		;;
esac

rm -rf ../block.rlp
rm -rf cn/data/klay/chaindata/ cn/data/klay/LOCK cn/data/klay/transactions.rlp cn/data/keystore/UTC--* *.profile *.trace
cn/bin/kcn init --datadir cn/data genesis.json
cn/bin/kcnd start
echo "#### check the log"
echo "tail -f cn/data/kcn/logs/kcnd.out"
