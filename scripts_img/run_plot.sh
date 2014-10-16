for f in ./Ijma/*.tped.out.ihs.out; do
	picname=${f#./Ijma/} picname=${picname%.tped.out.ihs.out}
	python ./plot.py  "$f" "./Obiachevo/chr-${f#./Ijma/}" "./CEU/chr-${picname}.tped.ihs.out"  "$picname"
	done

