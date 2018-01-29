# Plot fluorescence for RFP with and without riboswitch

library(ggplot2)

# Read file into dataframe
file_name <- ("/Users/pauldonovan/Dropbox/Pauls_crap/Butler and Higgins Lab/TPP_Riboswitch/PlateReader/RFP/Ribo-and-NoRibo_TwoConcs_24hr_For-R.tsv")
d <- read.table(file_name, 
                header = TRUE, 
                sep = "\t", 
                check.names = FALSE, 
                stringsAsFactors = FALSE) 
dframe <- data.frame(d)

# Open PDF for plot
pdf("/Users/pauldonovan/Dropbox/Pauls_crap/Butler and Higgins Lab/TPP_Riboswitch/PlateReader/RFP/Ribo-and-NoRibo_TwoConcs_24hr_For-R.pdf",
    width=10,height=5)
# Generate plot
ggplot(data=dframe,
       aes(x=Time, #x axis is time
           y=Mean, #y axis is Mean
           group=dframe$Concentration,  #Group sample with same concentration together
           color=dframe$Concentration)) +  #Colour samples with same concentration the same
 geom_errorbar(aes(ymin=Mean-Standard.Deviation, ymax=Mean+Standard.Deviation), width=1) +  #Generate Std Dev bars
 geom_line(size=0.5) +  #Width of lines
 geom_point(size=1) +    #Width of points
 theme(legend.title=element_blank()) +
 theme(axis.text.x=element_text(angle=90, hjust=1))   #Change x axis labelling format
dev.off()