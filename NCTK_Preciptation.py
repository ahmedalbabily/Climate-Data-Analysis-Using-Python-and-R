#import os
#import nctoolkit as nc
#import numpy as np
#os.chdir('/home/ahmedalbabili95/Desktop/')
#ff =  "file2.nc"
#ds = nc.open_data(ff)


#Plotting the firt ten years mean preciptation 

#ds.subset(years = range(1901, 1910))
#ds.subset(variables = "pre")
#ds.tmean()
#ds.plot()


#Plotting the last ten years mean preciptation 

#ds.subset(variables = "pre")
#ds.subset(years = range(2010, 2020))
#ds.tmean()
#ds.plot()

#Plotting the firt ten years mean preciptation/Winter Only

#ds.subset(years = range(1901, 1910))
#ds.subset(variables = "pre")
#ds.subset(season = "DJF")
#ds.tmean()
#ds.plot()

#Plotting the last ten years mean preciptation/Winter Only

#ds.subset(years = range(2010, 2020))
#ds.subset(variables = "pre")
#ds.subset(season = "DJF")
#ds.tmean()
#ds.plot()

#time_series

#ds.spatial_mean()
#ds.plot()


#Zonal_mean_first_10

#ds.subset(variables = "pre")
#ds.subset(years = range(1901, 1910))
#ds.tmean()
#ds.zonal_mean()
#ds.plot()

#Zonal_mean_last_10

#ds.subset(variables = "pre")
#ds.subset(years = range(2010, 2020))
#ds.tmean()
#ds.zonal_mean()
#ds.plot()

#yearly_time_series

#ds.tmean(["year"])
#ds.subset(variables = "pre")
#ds.spatial_mean()
#ds.plot()

#20_year_rolling_mean

#ds.subset(variables = "pre")
#ds.tmean(["year"])
#ds.spatial_mean()
#ds.rolling_mean(20)
#ds.plot()

#anomalies

#ds.annual_anomaly(baseline = [1901, 1920], window = 20)
#ds.spatial_mean()
#ds.plot()



#anomalies heatmap

mask = np.isnan(ds.data)

# mask the missing values in the data
ds.data = np.ma.masked_array(ds.data, mask)

# call the zonal_mean() and annual_anomaly() methods using the masked data
ds.zonal_mean()
ds.annual_anomaly(baseline = [1901, 1920], window = 20)

ds.plot()	



