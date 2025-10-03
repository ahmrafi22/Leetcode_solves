public class Solution
{
    public int[] CountBits(int n)
    {
        int[] arr = new int[n + 1]; 
        
        for (int i = 0; i <= n; i++)
        {
            
            arr[i] = Convert.ToString(i, 2)
                             .Replace("0", "")
                             .Length;
        }
        
        return arr;
    }
}
