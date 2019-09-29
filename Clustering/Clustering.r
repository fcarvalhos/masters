
#create data set with selected features

feature_selected_file_k3 = final_file[,c("difNLOC", "TotalTimeSpent")]
d = dist(feature_selected_file_k3, method = "euclidean")
clust <-hclust(d, method = "ward.D2")
sub_cluster<- cutree(clust, k = 3)

temp_file<-cbind(feature_selected_file_k3,sub_cluster)

studentID<- final_file[,1]
atv<- final_file[,6]
studentID<-cbind(studentID, temp_file)
studentID<-cbind(studentID, atv)


write.table(rbind(studentID), file = "mypath\\dNLoc_K4.csv", row.names = FALSE, sep = ",", col.names = TRUE)

current_file = read.csv("mypath\\dNLoc_K4.csv", header = TRUE, sep = ",")
