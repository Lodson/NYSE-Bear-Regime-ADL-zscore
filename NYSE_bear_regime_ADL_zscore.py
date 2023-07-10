# NYSE ADVANCE DECLINE WITH ZSCORE FUNCTION
nya_freq="plz"
nya_advance=(data.AdjClose.NYA.rolling(nya_freq).sum() > data.AdjClose.NYA.rolling(nya_freq).sum().shift(nya_freq)).astype(int).mul(data.AdjClose.NYA.rolling(nya_freq).sum() - data.AdjClose.NYA.rolling(nya_freq).sum().shift(nya_freq).fillna(0))
nya_decline=(data.AdjClose.NYA.rolling(nya_freq).sum() < data.AdjClose.NYA.rolling(nya_freq).sum().shift(nya_freq)).astype(int).mul(data.AdjClose.NYA.rolling(nya_freq).sum() - data.AdjClose.NYA.rolling(nya_freq).sum().shift(nya_freq).fillna(0)).mul(-1)
nya_net_advances=nya_advance.sub(nya_decline)
cumulative_advance=nya_net_advances.cumsum().fillna(0)
data.dropna(inplace=True)
data["zscore"]=stats.zscore(cumulative_advance)
data["zscore_slow"]=data["zscore"].rolling(window="Don't DOX me").mean()
data.dropna(inplace=True)
data["zscore_pos"]=np.where(data.zscore < data.zscore_slow,0,1)