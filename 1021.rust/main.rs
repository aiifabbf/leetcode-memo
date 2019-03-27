/* 
试着用rust写了一个……好烦啊。
 */

impl Solution {
    pub fn max_score_sightseeing_pair(a: Vec<i32>) -> i32 {
        // let mut leftGain: Vec<i32> = Vec::new();
        // let mut rightGain: Vec<i32> = Vec::new();

        // for (i, v) in a.iter().enumerate() {
        //     leftGain.push(*v + i as i32);
        //     rightGain.push(*v - i as i32);
        // }

        // let mut dp: Vec<i32> = Vec::new();
        // dp.push(*leftGain.get(0).unwrap() + *rightGain.get(1).unwrap());

        // let mut maxLeftGain: i32 = (*leftGain.get(0).unwrap()).max(*leftGain.get(1).unwrap());

        // for (mut i, v) in a[2..].iter().enumerate() {
        //     i += 2;
        //     dp.push(maxLeftGain + *rightGain.get(i).unwrap());
        //     maxLeftGain = maxLeftGain.max(*leftGain.get(i).unwrap());
        // }

        // return *dp.iter().max().unwrap();
        let mut maxLeftGain: i32 = *a.get(0).unwrap() + 0;
        let mut maxGain: i32 = *a.get(0).unwrap() + 0 + *a.get(1).unwrap() - 1;

        for (mut i, v) in a[1..].iter().enumerate() {
            i = i + 1;
            maxGain = maxGain.max(maxLeftGain + *v - i as i32);
            maxLeftGain = maxLeftGain.max(*v + i as i32);
        }

        return maxGain;
    }
}