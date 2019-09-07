class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        vector<int> help(nums.size()+1,0);
        help[1] = nums[0];
        int maxlen = 1;
        for(int i= 1;i<nums.size();i++) {
            int left = 1;
            int right = maxlen;
            while(left<=right) {//二分查找
                int mid = (left+right)/2;
                if(help[mid]<nums[i])
                    left = mid+1;
                else
                    right = mid-1;
            }
            // 找不到时怎么处理?  j = left - 1
            help[left] = nums[i];//维护help数组
            if(left>maxlen)//left值是nums[i]的子序列长度
                maxlen=left;
        }
        return maxlen;
    }
};