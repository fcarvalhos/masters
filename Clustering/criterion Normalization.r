
#Criterion Normalization 


final_file = read.csv("mypath\all_atvs.csv", header = TRUE, sep = ",")
destiny_file = "mypath\\Criterion_Normalization.csv"
header = c("F","C1","PBM")
write.table(rbind(header), file = destiny_file, row.names = FALSE, sep =",", col.names = TRUE)

features = c("difNLOC","Total.Time.Spent","Window")

#line
for(i in 1:length(features)){
    features1 = combn(features,i)
    for(k in 1:ncol(features1)){
         f1 = c()
         for(m in 1:nrow(features1)){
             f1 = c(f1,features1[m,k])
             }
              temp = final_file[,c(f1)]
              kclust <- kmeans(temp, centers = 4, iter.max = 30, nstart = 25)
              
             
              #column
              for(j in 1:length(features)){
              features2 = combn(features,j)
              for(r in 1:ncol(features2)){
                f2 = c()
                for(n in 1:nrow(features2)){
                  f2 = c(f2,features2[n,r])
                }
                csv_to_matrix = data.matrix(final_file[,c(f2)])
                pbm = clusterCrit::intCriteria(csv_to_matrix, kclust$cluster,"PBM")
                norm_row = c(paste(f1, collapse = " "), paste(f2, collapse = " "), pbm$pbm)
                
                write.table(rbind(norm_row), file = destiny_file, row.names = FALSE, sep =",",col.names = FALSE, append = TRUE)
                
                }
            }
          }
        }
