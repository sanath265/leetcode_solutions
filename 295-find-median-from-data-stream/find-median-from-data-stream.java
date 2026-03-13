class MedianFinder {

    private final Queue<Integer> maxHeap;
    private final Queue<Integer> minHeap;

    public MedianFinder() {
        maxHeap=new PriorityQueue<>(Comparator.reverseOrder());
        minHeap=new PriorityQueue<>();
    }
    
    void rebalance(){

        if(maxHeap.size()-minHeap.size()>1){
            minHeap.offer(maxHeap.poll());
        }

        if(minHeap.size() > 0 && maxHeap.peek()>=minHeap.peek()){
            minHeap.offer(maxHeap.poll());
        }
        
        if(minHeap.size()-maxHeap.size()>1){
            maxHeap.offer(minHeap.poll());
        }
        // if(maxHeap.size()+1>minHeap.size()){
        //     minHeap.offer(maxHeap.poll());
        // }else if(maxHeap.size()<minHeap.size()){
        //     maxHeap.offer(minHeap.poll());
        // }
    }

    public void addNum(int num) {
        maxHeap.offer(num);
        rebalance();
    }
    
    public double findMedian() {
        if(maxHeap.size()==minHeap.size()){
            return ((1.0)*maxHeap.peek()+minHeap.peek())/2;
        }else{
            // return 1.0*(minHeap.peek());
            // System.out.println(minHeap);
            // System.out.println(maxHeap);
            if (minHeap.size() > maxHeap.size()) {
                return 1.0*(minHeap.peek());
            } else {
                return 1.0*(maxHeap.peek());
            }
            
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */