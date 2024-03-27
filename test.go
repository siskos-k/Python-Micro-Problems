package main

import (
    "testing"
)

func MinRewards(scores []int) int {
    rewards := make([]int, len(scores))
    fill(rewards, 1)
    for i := 1; i < len(scores); i++ {
        if scores[i] > scores[i-1] {
            rewards[i] = rewards[i-1] + 1
        }
    }
    for i := len(scores) - 2; i >= 0; i-- {
        if scores[i] > scores[i+1] {
            rewards[i] = max(rewards[i], rewards[i+1]+1)
        }
    }
    return sum(rewards)
}

func MinRewards1(scores []int) int {
    rewards := make([]int, len(scores))
    fill(rewards, 1)
    localMinIndices := getLocalMinIndices(scores)
    for _, localMinIdx := range localMinIndices {
        expandFromLocalMinIdx(localMinIdx, scores, rewards)
    }
    return sum(rewards)
}

func getLocalMinIndices(arr []int) []int {
    localMinIndices := make([]int, 0)
    if len(arr) == 1 {
        localMinIndices = append(localMinIndices, 0)
        return localMinIndices
    }

    for i := 0; i < len(arr); i++ {
        if i == 0 && arr[i] < arr[i+1] {
            localMinIndices = append(localMinIndices, i)
        }
        if i == len(arr)-1 && arr[i] < arr[i-1] {
            localMinIndices = append(localMinIndices, i)
        }
        if i == 0 || i == len(arr)-1 {
            continue
        }
        if arr[i] < arr[i+1] && arr[i] < arr[i-1] {
            localMinIndices = append(localMinIndices, i)
        }
    }
    return localMinIndices
}

func expandFromLocalMinIdx(localMinIdx int, scores, rewards []int) {
    leftIdx := localMinIdx - 1
    for leftIdx >= 0 && scores[leftIdx] > scores[leftIdx+1] {
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx+1]+1)
        leftIdx--
    }

    rightIdx := localMinIdx + 1
    for rightIdx < len(scores) && scores[rightIdx] > scores[rightIdx-1] {
        rewards[rightIdx] = rewards[rightIdx-1] + 1
        rightIdx++
    }
}

func fill(arr []int, val int) {
    for i := range arr {
        arr[i] = val
    }
}

func sum(arr []int) int {
    sum := 0
    for i := range arr {
        sum += arr[i]
    }
    return sum
}

func max(i, j int) int {
    if i > j {
        return i
    }
    return j
}

func minRewards(scores []int) int {
    if len(scores) == 1 {
        return 1
    }

    peaks := make(map[int][]int)
    var i int
    for i < len(scores)-1 {
        if scores[i] < scores[i+1] {
            left, peak := i, i
            for peak < len(scores)-1 && scores[peak] < scores[peak+1] {
                peak++
            }

            right := peak
            for right < len(scores)-1 && scores[right] > scores[right+1] {
                right++
            }
            i = right

            peaks[peak] = append([]int{}, []int{left, right}...)
        } else {
            peak, right := i, i
            for right < len(scores)-1 && scores[right] > scores[right+1] {
                right++
            }
            i = right
            peaks[peak] = append([]int{}, []int{peak, right}...)
        }
    }

    ranges := make(map[int]int)
    var minRewards int
    for k, val := range peaks {
        left := val[0]
        peak := k
        right := val[1]

        ranges[left]++
        ranges[right]++

        if right-peak > peak-left {
            peakReward := right - peak + 1
            rightReward := 1
            minRewards += (peakReward + rightReward) * peakReward / 2

            maxLeftReward := peak - left
            leftReward := 1
            minRewards += (leftReward + maxLeftReward) * maxLeftReward / 2
        } else {
            peakReward := peak - left + 1
            leftReward := 1
            minRewards += (peakReward + leftReward) * peakReward / 2

            maxRightReward := right - peak
            rightReward := 1
            minRewards += (rightReward + maxRightReward) * maxRightReward / 2
        }
    }

    for _, v := range ranges {
        if v > 1 {
            minRewards -= 1
        }
    }

    return minRewards
}

// Testing

// TestMinRewards tests the first implementation of the MinRewards function.
func TestMinRewards(t *testing.T) {
    tests := []struct {
        scores  []int
        rewards int
    }{
        {[]int{8, 4, 2, 1, 3, 6, 7, 9, 5}, 25}, // Basic case
        {[]int{1}, 1},                          // Single element
        {[]int{5, 10}, 3},                      // Two elements increasing
        {[]int{10, 5}, 3},                      // Two elements decreasing
        {[]int{4, 3, 2, 1, 2, 3, 4}, 16},       // V shape
        // Add more cases here to cover different scenarios
    }

    for _, tc := range tests {
        t.Run("", func(t *testing.T) {
            got := MinRewards(tc.scores)
            if got != tc.rewards {
                t.Errorf("MinRewards(%v) = %d; want %d", tc.scores, got, tc.rewards)
            }
        })
    }
}

// TestMinRewards1 tests the second implementation of the MinRewards function.
func TestMinRewards1(t *testing.T) {
    tests := []struct {
        scores  []int
        rewards int
    }{
        {[]int{8, 4, 2, 1, 3, 6, 7, 9, 5}, 25}, // Basic case
        {[]int{1}, 1},                          // Single element
        {[]int{5, 10}, 3},                      // Two elements increasing
        {[]int{10, 5}, 3},                      // Two elements decreasing
        {[]int{4, 3, 2, 1, 2, 1, 2, 3, 4}, 16}, // V shape
                       // Add more cases here to cover different scenarios
                   }

                   for _, tc := range tests {
                       t.Run("", func(t *testing.T) {
                           got := MinRewards1(tc.scores)
                           if got != tc.rewards {
                               t.Errorf("MinRewards1(%v) = %d; want %d", tc.scores, got, tc.rewards)
                           }
                       })
                   }
               }

               // TestMinRewards2 tests the third implementation (named as minRewards in the provided code)
               // of the MinRewards function.
               func TestMinRewards2(t *testing.T) {
                   tests := []struct {
                       scores  []int
                       rewards int
                   }{
                       {[]int{8, 4, 2, 1, 3, 6, 7, 9, 5}, 25}, // Basic case
                       {[]int{1}, 1},                          // Single element
                       {[]int{5, 10}, 3},                      // Two elements increasing
                       {[]int{10, 5}, 3},                      // Two elements decreasing
                       {[]int{4, 3, 2, 1, 2, 3, 4}, 16},       // V shape
                       // Add more cases here to cover different scenarios
                   }

                   for _, tc := range tests {
                       t.Run("", func(t *testing.T) {
                           got := minRewards(tc.scores)
                           if got != tc.rewards {
                               t.Errorf("minRewards(%v) = %d; want %d", tc.scores, got, tc.rewards)
                           }
                       })
                   }
               }

               // Add additional tests if needed to cover edge cases, such as:
               // - Large input arrays to test performance implications.
               // - Arrays with all elements being the same.
               // - Arrays with a large number of elements, but only two distinct scores.
               func TestEdgeCases(t *testing.T) {
                   // Implement additional tests here.
               }

               func main() {
                   // Run tests
                   testFunctions := []testing.InternalTest{
                       {Name: "TestMinRewards", F: TestMinRewards},
                       {Name: "TestMinRewards1", F: TestMinRewards1},
                       {Name: "TestMinRewards2", F: TestMinRewards2},
                       // Add more test functions here if needed
                   }

                   match := func(pat, str string) (bool, error) {
                       return true, nil
                   }

                   testing.Main(match, testFunctions, nil, nil)
               }
