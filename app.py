import streamlit as st

# 초기 설정: 세션에 todo 리스트가 없으면 초기화
if 'todos' not in st.session_state:
    st.session_state.todos = []  # 각 아이템은 {'task': str, 'completed': bool}

st.title('🗒️ 할 일 관리')
st.caption('세션 상태에 저장되는 간단한 To‑Do 앱')

# 새 할 일 추가 UI
new_task = st.text_input('새 할 일 추가', placeholder='예: 코드 공부')
add_clicked = st.button('추가')
if add_clicked and new_task:
    st.session_state.todos.append({'task': new_task, 'completed': False})
    st.success('추가되었습니다!')
    # 입력창 초기화 (페이지 재렌더링 시 자동 초기화)
    st.experimental_rerun()

# 할 일 리스트 표시 및 체크박스 처리
if st.session_state.todos:
    for idx, item in enumerate(st.session_state.todos):
        cols = st.columns([0.05, 0.8, 0.15])
        with cols[0]:
            # 완료 체크박스
            checked = st.checkbox('', value=item['completed'], key=f'completed_{idx}')
            st.session_state.todos[idx]['completed'] = checked
        with cols[1]:
            # 텍스트 표시 (완료 시 취소선)
            if item['completed']:
                st.markdown(f"~~{item['task']}~~")
            else:
                st.write(item['task'])
        with cols[2]:
            # 삭제 버튼
            if st.button('🗑️', key=f'delete_{idx}'):
                st.session_state.todos.pop(idx)
                st.experimental_rerun()
else:
    st.info('할 일이 없습니다.')

# 완료/미완료 개수 요약 표시
completed_cnt = sum(1 for t in st.session_state.todos if t['completed'])
remaining_cnt = len(st.session_state.todos) - completed_cnt
st.divider()
st.write(f"✅ 완료된 작업: {completed_cnt} 개")
st.write(f"🕒 남은 작업: {remaining_cnt} 개")
