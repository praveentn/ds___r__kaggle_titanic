# Create a sample of 5000 numbers which are normally distributed
# with mean of 777 and standard deviation of 100
# rnorm() is used to generate random numbers whose distribution is normal
# arguments to this function are in the order sample size, mean and S.D.
y <- rnorm(5000, 777, 100)

# Give the chart file a name
png(file = "normal_dist_with_mean_and_sd.png")

# Verify the sample; plot first 100 samples
plot(y[1:100])

# Plot the histogram for this sample 'y'
hist(y, main = "Normal Distribution")

# Saves the file
dev.off()

# output: refer "normal_dist_with_mean_and_sd.png"
