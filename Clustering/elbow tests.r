clusters_data_file_header = c("features", "NFeatures", "pbm", "Silhuette")
final_file = read.csv("mypath\\final_file.csv", header = TRUE, sep = ",")
header_df = c("difNLOC","submissions","Window","Total.Time.Spent")
#colnames(final_file)
#generate all test for K=1...4 based on the elbow tests previously done

for(cl in 2:6){
  
  #clusters_data_file = paste("mypath\\Kmeans_Cluster_eval_k_", cl,".csv", sep = "")
  clusters_data_file = paste("mypath\\ward_Cluster_eval_k_", cl,".csv", sep = "")
  write.table(rbind(clusters_data_file_header), file = clusters_data_file, row.names=FALSE, append = TRUE, sep =",", col.names = FALSE)
  
  #creates a combination of all possible data frames from a set os columns with variable group number from 1 to header elements(7)
  
  for (i in 1:length(header_df)){
    
    j<-combn(header_df,i)
    
    #creates a temp file, with the same entrances (nrows) as the original final and columns as the current group (1 to 7)
    
    temp_file= data.frame(matrix(ncol= 0, nrow = nrow(final_file)))
    
    #Runs through columns names and copy that column to the tempfile creating a file with a subgroup of columns to be analyzed
    
    for(h in 1:ncol(j)){
      column_names = c()
      for(k in 1:nrow(j)){
      column_names = c(column_names,j[k,h])
      }
      
      temp_file = final_file[,c(column_names)]
      
      #generate optimal cluster analysis based on elbow
      
      used_features  = paste(column_names, collapse = ",")
      
      #Ward
      img_name = paste("mypath\\Cluster_Feature_Analysis WARD\\elbow_",used_features,".png")
      ggsave(filename = img_name, plot = fviz_nbclust(data.matrix(temp_file), FUN = hcut, method = "wss"))
      
      #Kmeans
      #img_name = paste("mypath\\Cluster_Feature_Analysis Kmeans\\elbow_",used_features,".png")
      #ggsave(img_name, plot = fviz_nbclust(data.matrix(temp_file), kmeans, method = "wss"))
      
      
      #after each subgroup is created, calculate the distance matrix and create the clusters
      
      
      #ward
      d = dist(temp_file, method = "euclidean")
      clust <-hclust(d, method = "ward.D2")
      sub_cluster<- cutree(clust, k = cl)
      
      #Kmeans
      #kclust <- kmeans(temp_file, centers = cl, iter.max = 30, nstart = 25)
      
      #evaluate the clusters
      csv_to_matrix = data.matrix(temp_file)
      
      #ward
      pbm = clusterCrit::intCriteria(csv_to_matrix, sub_cluster, "PBM")
      Ball_and_Hall = clusterCrit::intCriteria(csv_to_matrix, sub_cluster, "Ball_Hall")
      
      #kmeans
      #pbm = clusterCrit::intCriteria(csv_to_matrix, kclust$cluster, "PBM")
      #Ball_and_Hall = clusterCrit::intCriteria(csv_to_matrix, kclust$cluster, "Ball_Hall")
      
      #if(pbm$pbm> 0.43){
        #img_hclust = paste("mypath\\Cluster_Feature_Analysis WARD\\Kmeans_",used_features,"_",cl,".png")
        #ggsave(filename = img_hclust, plot = plot(clust, cex = 0.6))
        #ggsave(filename = img_hclust, plot = plot(temp_file, col = kclust$cluster))
      
      #}
      
      
      stats = c(paste(column_names, collapse = " "), length(column_names) ,pbm$pbm, Ball_and_Hall$ball_hall)
      
      
      #write the columns names and the evaluation results to the file 
      write.table(rbind(stats), file = clusters_data_file, row.names=FALSE, append = TRUE, sep =",", col.names = FALSE)
      
    }
  
  }
}
