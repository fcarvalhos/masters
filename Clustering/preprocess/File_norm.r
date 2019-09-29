
files <- list.files(path=mypath\\",full.names =TRUE, recursive =FALSE)
file_name <-paste("mypath\\", atv,"norm.csv", sep = ",")
normalize<- function(x){
return((x - min(x))/ (max(x) - min(x)))
}
for(f in files){
path = paste(f, sep="")
Atv_folder<-Sys.glob(path)
atv <- strsplit(Atv_folder,"\\\\")[[1]][9]
atv <-strsplit(atv,",.")[[1]][1]
file_name <-paste("mypath\\", atv,"norm.csv", sep = "")
atv_file <- read.csv(f, header = TRUE, sep = ",")
atv_file_norm<- as.data.frame(lapply(atv_file[,7:16], normalize))
studentID<- atv_file[,1:6]
studentID<-cbind(studentID, atv_file_norm)
write.table(rbind(studentID), file = file_name, row.names=FALSE, append = TRUE, sep =",", col.names = TRUE)
}
