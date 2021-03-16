#sch is the actual network given

#saving the network as a edge list file
a = as.matrix.network(sch, matrix.type = 'edgelist')
write.table(a, file = '../Dropbox/AddHealth_Data/folder/school.txt', 
            row.names = FALSE, col.names = FALSE)

# this FMH network is a representative network of the actual data available in the literature. Here I extract it and save it as an edge list file

fmh = faux.magnolia.high
fmhn = as.matrix.network(fmh, matrix.type = 'edgelist')
write.table(fmhn, file = '../Dropbox/AddHealth_Data/folder/fmh.txt', 
            row.names = FALSE, col.names = FALSE)
