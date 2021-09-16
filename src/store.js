import { createStore } from 'vuex'
import axios from 'axios'

const store = createStore({
	// 데이터
	state () {
		return {
			name : 'kim',
			age : 20,
			likes : [30, 10, 20],
			isLiked : [false, false, false],
			more : {},
		}
	},

	// 함수
	mutations : {
		setMore(state, data) {
			state.more = data
		},
		changeName(state) {
			if (state.name === 'kim') {
				state.name = 'park'
			} else {
				state.name = 'kim'
			}
		},
		addAge(state, payload) {
			state.age += payload
		},
		likeOnOff(state, index) {
			if (state.isLiked[index] === false) {
				state.likes[index]++
				state.isLiked[index] = true
			} else {
				state.likes[index]--
				state.isLiked[index] = false
			}
		},
	},

	// ajax 요청
	actions : {
		getData(context) {
			axios.get('https://codingapple1.github.io/vue/more0.json')
			.then((result) => {
				context.commit('setMore', result.data);
			})
		},
	},
})

export default store;