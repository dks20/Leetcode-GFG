class Solution {
    public int[] sortArray(int[] nums) {
        int n = nums.length -1;
        mergeSort(nums,0,n);
        return nums;
        
    }
    public void merged(int arr[],int s,int mid,int e){

        int[] merged = new int[e-s +1];

        int idx1 = s;
        int idx2 = mid+1;
        int x =0;

        while(idx1 <= mid && idx2 <= e){
            if(arr[idx1] <= arr[idx2]){
                merged[x++] = arr[idx1++];
            }else{
                merged[x++] = arr[idx2++];
            }
        }
        while(idx1 <= mid){
            merged[x++] = arr[idx1++];
        }
        while(idx2 <= e){
            merged[x++] = arr[idx2++];
        }

        for(int i = 0,j =s;i<merged.length;i++,j++){
            arr[j] = merged[i];
        }


    }

    public void mergeSort(int arr[],int s, int e){
        if(s >= e){
            return;
        }
        int mid = s + (e-s)/2;
        mergeSort(arr,s,mid);
        mergeSort(arr,mid+1,e);

        merged(arr,s,mid,e);

    }

    
}