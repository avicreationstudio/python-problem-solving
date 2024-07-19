# below are different condition for different patterns

1. `if (i - j >= 0 || i + j <= n - 1)`
1. `if (i - j <= 0 || i + j >= n - 1)`
1. `if (i - j >= 0 && i + j <= n - 1)`
1. `if (i - j <= 0 && i + j >= n - 1)`
1. `if ((i-j>=0 && i+j<=n-1)||(i-j<=0&&i+j>=n-1))`
1. `if (i - j <= 0 || i + j <= n - 1)`
1. `if (i - j >= 0 || i + j >= n - 1)`
1. `if (i - j <= 0 && i + j <= n - 1)`
1. `if (i - j >= 0 && i + j >= n - 1)`
1. `if ((i-j<=0 && i+j<=n-1)||(i-j>=0 &&i+j>=n-1))`
1. `if (i==0||j==0||i==n-1||j==n-1)`
1. `if (i==0||j==0||i==n-1||j==n-1||i+j==n-1||i-j==0)`
1. `if (i + j >= (n - 1) / 2)`
1. `if (i + j <= (n - 1) + ((n-1) / 2))`
1. `if (i - j >= -((n - 1) / 2))`
1. `if (i - j <= ((n - 1) / 2))`
1. `if ((i+j>=(n-1)/2)&&(i+j<=(n-1)+((n-1)/2))&&(i-j>=-((n-1)/2))&&(i-j<=((n-1)/2)))`
